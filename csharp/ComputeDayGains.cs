using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    public static int ComputeDayGains(int nbSeats, int[] payingGuests, int[] guestMovements)
    {
        int[] seats = new int[nbSeats]; // array to keep track of which seats are occupied
        Dictionary<int, int> guestPayments = new Dictionary<int, int>(); // dictionary to keep track of how much each guest has paid
        int gains = 0; // variable to keep track of the gains for the day

        for (int i = 0; i < guestMovements.Length; i++)
        {
            int guestId = guestMovements[i];

            if (guestId < 0) // departure
            {
                int seatNumber = -guestId - 1; // seat number is stored as the opposite of the guest id minus 1
                seats[seatNumber] = 0; // free the seat
            }
            else // arrival
            {
                int guestPayment;
                if (guestPayments.TryGetValue(guestId, out guestPayment)) // guest has already paid
                {
                    continue; // skip this arrival
                }

                int seatNumber = -1; // index of the available seat
                for (int j = 0; j < nbSeats; j++)
                {
                    if (seats[j] == 0) // seat is available
                    {
                        seatNumber = j;
                        seats[j] = guestId; // occupy the seat
                        break;
                    }
                }

                if (seatNumber >= 0) // guest found a seat
                {
                    guestPayments.Add(guestId, payingGuests[guestId]); // add the guest to the list of paying guests
                    gains += payingGuests[guestId]; // update the gains
                }
            }
        }

        return gains;
    }

    /* Ignore and do not change the code below */
    static void Main(string[] args)
    {
        string[] inputs;
        int nbSeats = int.Parse(Console.ReadLine());
        int nbGuests = int.Parse(Console.ReadLine());
        int nbMovements = int.Parse(Console.ReadLine());
        int[] payingGuests = new int[nbGuests];
        inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < nbGuests; i++)
        {
            payingGuests[i] = int.Parse(inputs[i]);
        }
        int[] guestMovements = new int[nbMovements];
        inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < nbMovements; i++)
        {
            guestMovements[i] = int.Parse(inputs[i]);
        }
        var stdtoutWriter = Console.Out;
        Console.SetOut(Console.Error);
        int res = ComputeDayGains(nbSeats, payingGuests, guestMovements);
        Console.SetOut(stdtoutWriter);
        Console.WriteLine(res);
    }
    /* Ignore and do not change the code above */
}