#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

int main()
{
    // Ruta del directorio de entrada
    std::string ruta_dir;

    std::cout << "Enter directory: ";
    std::getline(std::cin, ruta_dir);

    std::cout << "\n------------------------------------\n";

    // Recorrer todos los archivos en la carpeta
    for (const std::filesystem::directory_entry &entrada : std::filesystem::directory_iterator(ruta_dir))
    {
        // Archivo y no otro tipo
        if (entrada.is_regular_file())
        {
            std::ifstream archivo(entrada.path());

            // Verifica si se puede abrir el archivo
            if (archivo)
            {
                std::string contenido_val((std::istreambuf_iterator<char>(archivo)), std::istreambuf_iterator<char>());

                // Imprimir el nombre y el contenido del archivo
                std::cout << entrada.path().filename().string() << "\n\n";
                std::cout << contenido_val << "\n";
                std::cout << "------------------------------------\n";
            }
        }
    }

    // Espera a que el usuario presione Enter antes de cerrar
    std::cin.get();

    return 0;
}
