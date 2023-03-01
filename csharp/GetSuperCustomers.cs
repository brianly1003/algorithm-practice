using System;
using System.Linq;
using System.Collections.Generic;

class Order
{
    public string Customer { get; set; }
    public decimal Price { get; set; }
}

class Program
{
    /// <returns>an enumeration of the names of "super"​​​​​​‌​​‌‌‌‌‌‌‌‌​‌​‌​‌​‌‌‌‌‌​‌ customers</returns>
	public static IEnumerable<string>
    GetSuperCustomers(List<Order> orders)
    {
        // Group the orders by customer and compute the total price for each customer
        var customerGroups = orders.GroupBy(o => o.Customer)
                                   .Select(g => new { Customer = g.Key, TotalPrice = g.Sum(o => o.Price) });

        // Filter the customer groups to include only those with a total price of at least 100
        var superCustomerGroups = customerGroups.Where(g => g.TotalPrice >= 100);

        // Extract the names of the super customers from the filtered customer groups
        var superCustomers = superCustomerGroups.Select(g => g.Customer);

        // Return the names of the super customers as an enumeration
        return superCustomers;
    }
}