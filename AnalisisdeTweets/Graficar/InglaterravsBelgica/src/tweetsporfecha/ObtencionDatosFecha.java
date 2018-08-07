package tweetsporfecha;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;
import java.util.Random;


public class ObtencionDatosFecha {

	static String Pais1;
	static String Pais2;
	static int nDeTweets1 = 0 ;
	static String tweetsPais1;
	static int nDeTweets2 = 0 ;
	static String tweetsPais2;
	static Hashtable<String, Integer> fechasPais2 = new Hashtable<String, Integer>();
	static Hashtable<String, Integer> fechasPais = new Hashtable<String, Integer>();
	public static void pais1(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\fechasIng.txt");
		FileReader fileR = null;
		BufferedReader file2 = null;

		try {
			fileR = new FileReader(file);
			file2 = new BufferedReader(fileR);
			String name = file.getName();
			 Pais1 = name.substring(name.length() - 7, name.length()-3);
			System.out.println(Pais1);
		
		} catch (FileNotFoundException e) {
			System.out.println("No se encontro el archivo "+file.getName());

		}

		try {
			String lines = "";
			int valor =0;
			while( ( lines = file2.readLine()) != null) {
				nDeTweets1 = nDeTweets1 +1;
				
				//for (int i=0; i<2363;i++ ){
				//int numero = (int) (Math.random() * 2) + 1;
						
				//if (numero == 1){
				String[] partes = lines.split(",");
				//System.out.println(partes[0]);
				if (fechasPais.get(partes[0])== null){
					fechasPais.put(partes[0], 1);
					
				}
				else{
				valor = fechasPais.get(partes[0]) ;
				valor = valor +1;
				fechasPais.put(partes[0], valor);
				//}
				//	}
				}


			}
			tweetsPais1 = Pais1 + ":" + String.valueOf(nDeTweets1);
			
			//System.out.println("Francia"+"1:" +hora1F +" "+"2:" +hora2F +" "+"3:"+ hora3F);
		}catch (IOException e) {
			e.printStackTrace();
		}
	
	}

	public static void pais2(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\fechasBel.txt");
		FileReader fileR = null;
		BufferedReader file2 = null;

		try {
			fileR = new FileReader(file);
			file2 = new BufferedReader(fileR);
			String name = file.getName();
			 Pais2 = name.substring(name.length() - 7, name.length()-3);
			System.out.println(Pais2);

		} catch (FileNotFoundException e) {
			System.out.println("No se encontro el archivo "+file.getName());

		}

		try {
			String lines = "";
			int valor =0;
			String []matriz = new String[8000] ;
			for (int indice = 1 ;indice<7911; indice++){
			//int numero = (int) Math.floor((Math.random() * 2) + 1);
			//if ( numero ==1 ){
			
				while( ( lines = file2.readLine()) != null){
	
				nDeTweets2 = nDeTweets2 +1; 
				String[] partes = lines.split(",");

					if (fechasPais2.get(partes[0])== null){
						fechasPais2.put(partes[0], 1);
					}
					else{
					valor = fechasPais2.get(partes[0]) ;
					valor = valor +1;
					fechasPais2.put(partes[0], valor);
					}
			
					}
			//i++;		
			}
					
			
			System.out.println(fechasPais2 + "espacio" + fechasPais);
			tweetsPais2 = Pais2 + ":" + String.valueOf(nDeTweets2);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}
}



