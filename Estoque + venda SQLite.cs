using Microsoft.Data.Sqlite;
using Negocio;
using SQLitePCL;
using System;
using System.Collections.Generic;

namespace Negocio
{
    class ExceptionVenda : Exception
    {
        public ExceptionVenda(string message) : base(message)
        {
        }
    }

    public class Empresa
    {
        public decimal Saldo { get; private set; } = 10000m;

        public void RegistrarVenda(decimal valor)
        {
            if (valor <= 0)
                throw new ExceptionVenda("Valor inválido!");

            Saldo += valor;
        }
    }

    public class Produto
    {
        public int Id { get; set; }

        public string Nome { get; set; }

        public decimal Preco { get; set; }

        public int Estoque { get; set; }

        public void ReduzirEstoque(int quantidade)
        {
            if (quantidade <= 0)
                throw new ExceptionVenda("Quantidade inválida!");

            if (quantidade > Estoque)
                throw new ExceptionVenda("Estoque insuficiente!");

            Estoque -= quantidade;
        }

        public void AdicionarEstoque(int quantidade)
        {
            if (quantidade <= 0)
                throw new ExceptionVenda("Quantidade inválida!");

            Estoque += quantidade;
        }
    }

    public class Venda
    {
        public Produto Produto { get; set; }

        public int Quantidade { get; set; }

        public decimal Total => Produto.Preco * Quantidade;
    }

    class Program
    {
        static void Main(string[] args)
        {
            Batteries.Init();

            Empresa empresa = new Empresa();

            List<Produto> produtos = new List<Produto>();

            string conexao =
                @"Data Source=C:\Users\VictorFerreiraGuimar\Documents\Ronaldobase.db";

            SqliteConnection conn =
                new SqliteConnection(conexao);

            try
            {
                conn.Open();

                Console.WriteLine("Conectado ao SQLite brabo");

                string criarTabela =
                @"
                CREATE TABLE IF NOT EXISTS produtos
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    preco REAL,
                    estoque INTEGER
                )
                ";

                SqliteCommand criarCmd =
                    new SqliteCommand(criarTabela, conn);

                criarCmd.ExecuteNonQuery();

                string verificar =
                    "SELECT COUNT(*) FROM produtos";

                SqliteCommand verificarCmd =
                    new SqliteCommand(verificar, conn);

                long totalProdutos =
                    (long)verificarCmd.ExecuteScalar();

                string inserir =
                @"
                INSERT INTO produtos(nome, preco, estoque)
                VALUES
                ('Machine1', 7400, 10),
                ('Machine2', 5000, 5),
                ('Machine3', 9000, 8),
                ('Headset', 500, 15),
                ('Mouse', 150, 20);
                ";

                if (totalProdutos == 0)
                {
                    SqliteCommand insertCmd =
                        new SqliteCommand(inserir, conn);

                    insertCmd.ExecuteNonQuery();
                }

                string sql = "SELECT * FROM produtos";

                SqliteCommand cmd =
                    new SqliteCommand(sql, conn);

                SqliteDataReader reader =
                    cmd.ExecuteReader();

                while (reader.Read())
                {
                    Produto produto = new Produto
                    {
                        Id = Convert.ToInt32(reader["id"]),
                        Nome = reader["nome"].ToString(),
                        Preco = Convert.ToDecimal(reader["preco"]),
                        Estoque = Convert.ToInt32(reader["estoque"])
                    };

                    produtos.Add(produto);
                }

                reader.Close();

                Console.WriteLine("\n=== PRODUTOS ===");

                foreach (var produto in produtos)
                {
                    Console.WriteLine(
                        $"{produto.Id} - " +
                        $"{produto.Nome} - " +
                        $"R${produto.Preco} - " +
                        $"Estoque: {produto.Estoque}"
                    );
                }

                Console.WriteLine("\n1 - Registrar venda");
                Console.WriteLine("2 - Adicionar estoque");

                if (!int.TryParse(Console.ReadLine(), out int opcao))
                    throw new FormatException();

                Console.WriteLine("\nDigite o ID do produto:");

                if (!int.TryParse(Console.ReadLine(), out int id))
                    throw new FormatException();

                Produto produtoEscolhido =
                    produtos.Find(p => p.Id == id);

                if (produtoEscolhido == null)
                    throw new ExceptionVenda("Produto não encontrado!");

                Console.WriteLine("Quantidade:");

                if (!int.TryParse(Console.ReadLine(), out int quantidade))
                    throw new FormatException();

                if (opcao == 1)
                {
                    produtoEscolhido.ReduzirEstoque(quantidade);

                    Venda venda = new Venda
                    {
                        Produto = produtoEscolhido,
                        Quantidade = quantidade
                    };

                    empresa.RegistrarVenda(venda.Total);

                    Console.WriteLine("\n=== VENDA REALIZADA ===");

                    Console.WriteLine($"Produto: {venda.Produto.Nome}");
                    Console.WriteLine($"Quantidade: {venda.Quantidade}");
                    Console.WriteLine($"Total: R${venda.Total}");

                    Console.WriteLine(
                        $"Saldo atual da empresa: R${empresa.Saldo}"
                    );
                }
                else if (opcao == 2)
                {
                    produtoEscolhido.AdicionarEstoque(quantidade);

                    Console.WriteLine("\n=== ESTOQUE ATUALIZADO ===");

                    Console.WriteLine(
                        $"{produtoEscolhido.Nome} agora possui " +
                        $"{produtoEscolhido.Estoque} unidades."
                    );
                }
                else
                {
                    throw new ExceptionVenda("Opção inválida!");
                }

                string atualizar =
                @"
                UPDATE produtos
                SET estoque = @estoque
                WHERE id = @id
                ";

                SqliteCommand updateCmd =
                    new SqliteCommand(atualizar, conn);

                updateCmd.Parameters.AddWithValue(
                    "@estoque",
                    produtoEscolhido.Estoque
                );

                updateCmd.Parameters.AddWithValue(
                    "@id",
                    produtoEscolhido.Id
                );

                updateCmd.ExecuteNonQuery();

                conn.Close();
            }
            catch (FormatException)
            {
                Console.WriteLine("Digite apenas números!");
            }
            catch (ExceptionVenda ex)
            {
                Console.WriteLine($"Erro: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Erro inesperado: {ex.Message}");
            }
        }
    }
}
/*Programa inicia
↓
Conecta no SQLite
↓
Cria tabela se não existir
↓
Insere produtos iniciais (uma vez)
↓
Busca produtos do banco
↓
Transforma linhas SQL em objetos C#
↓
Mostra produtos
↓
Usuário escolhe ação
↓
C# altera objeto
↓
UPDATE salva no banco
↓
Programa fecha*/
