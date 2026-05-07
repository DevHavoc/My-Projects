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
                throw new ExceptionVenda("Valor da venda inválido!");

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
    }

    public class Venda
    {
        public Produto Produto { get; set; }
        public int Quantidade { get; set; }
        public decimal Total => Produto.Preco * Quantidade;
    }

    public class VendaService
    {
        public void RegistrarVenda(Empresa empresa, Venda venda)
        {
            if (venda.Quantidade <= 0)
                throw new ExceptionVenda("Quantidade inválida!");

            venda.Produto.ReduzirEstoque(venda.Quantidade);

            empresa.RegistrarVenda(venda.Total);

            Console.WriteLine("\n=== VENDA REALIZADA ===");
            Console.WriteLine($"Produto: {venda.Produto.Nome}");
            Console.WriteLine($"Quantidade: {venda.Quantidade}");
            Console.WriteLine($"Total: R${venda.Total}");

            Console.WriteLine($"\nSaldo atual da empresa: R${empresa.Saldo}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Empresa empresa = new Empresa();

            List<Produto> produtos = new List<Produto>()
            {
                new Produto { Id = 1, Nome = "Machine1", Preco = 7400m, Estoque = 10 },
                new Produto { Id = 2, Nome = "Machine2", Preco = 5000m, Estoque = 5 },
                new Produto { Id = 3, Nome = "Machine3", Preco = 9000m, Estoque = 8 }
            };

            Console.WriteLine("=== PRODUTOS ===");

            foreach (var produto in produtos)
            {
                Console.WriteLine($"{produto.Id} - {produto.Nome} - R${produto.Preco} - Estoque: {produto.Estoque}");
            }

            try
            {
                Console.WriteLine("\nDigite o ID do produto:");

                int id = int.Parse(Console.ReadLine());

                Produto produtoEscolhido = produtos.Find(p => p.Id == id);

                if (produtoEscolhido == null)
                    throw new ExceptionVenda("Produto não encontrado!");

                Console.WriteLine("Quantidade:");

                int quantidade = int.Parse(Console.ReadLine());

                Venda venda = new Venda
                {
                    Produto = produtoEscolhido,
                    Quantidade = quantidade
                };

                VendaService service = new VendaService();

                service.RegistrarVenda(empresa, venda);
            }
            catch (FormatException)
            {
                Console.WriteLine("Digite apenas números!");
            }
            catch (ExceptionVenda ex)
            {
                Console.WriteLine($"Erro de venda: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Erro inesperado: {ex.Message}");
            }
        }
    }
}