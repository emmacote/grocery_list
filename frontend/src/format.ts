export const currencyFormatter = Intl.NumberFormat("en-US", {style: "currency", currency: "USD"});
export function toUSCurrency(price: number){
    return currencyFormatter.format(price);
}