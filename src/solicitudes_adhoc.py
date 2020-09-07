import matplotlib.pyplot as plt
import seaborn as sns

def barrio_distrito(df, zona):
    """
    Con esta función puedes saber los barrios que hay en cada distrito de Madrid:
    zona = distrito de Madrid
    """
    return df["barrio"][df.distrito == zona].unique()


def evolucion_precios_distrito(df, zona):
    """
    df = dataframe
    zona = distrito donde quieres ver la evolución del precio del m2 por barrio
    """
    evolucion = df[df.distrito == zona].groupby("barrio").eurosm2_barrio.mean()
    fig = plt.subplots(figsize = (8, 6))
    plt.plot(evolucion)
    plt.ylabel(f"Precio del m2 en €", fontsize = 12)
    plt.xticks(rotation = 90)
    plt.title(f"Evolución del precio por m2 según barrio de {zona}", fontsize = 15)


def opcion_barrio(df, bar):
    """
    Con esta función podrás ver un gráfico donde se muestran los activos en venta por barrios:
    bar = barrio de un distrito de Madrid
    """
    opciones_barrio = df[df.barrio == bar].reset_index()
    fig = plt.figure(figsize = (10,8))
    sns.scatterplot(x = "metros2_const", y = "precio_venta", data = opciones_barrio, hue = "n_habitaciones")
    plt.suptitle(f"PRECIO VENTA - M2 CONSTRUIDOS EN {bar}", y = 0.92, fontsize = 15)


def m2(df, zona, bar, hab, ban, m2, precio):
    """
    Con esta función podrás elegir el alojamiento que más se adecue a tus necesidades:
    df = Dataframe
    distrito = class str - Elija un distrito de Madrid
    bar = type str - barrio del distrito que eligió en distrito
    hab = type int - número mínimo de habitaciones
    ban = type int - número mínimo de baños
    m2 = type int - Elija los m2 minimos construidos
    precio = type int - precio máximo que está dispuesto a pagar
    """
    resultado = df[(df.distrito == zona) & (df.barrio == bar) & (df.n_habitaciones >= hab)& (df.n_banos >= ban) & (df.metros2_const > m2) & (df.precio_venta < precio)]
    return resultado