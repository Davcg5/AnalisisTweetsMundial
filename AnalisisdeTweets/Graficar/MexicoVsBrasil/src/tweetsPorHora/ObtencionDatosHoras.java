package tweetsPorHora;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;


public class ObtencionDatosHoras {
	
	static String Pais1;
	static String Pais2;
	static int nDeTweets1 = 0 ;
	static String tweetsPais1;
	static int nDeTweets2 = 0 ;
	static String tweetsPais2;
	static Hashtable<String, Integer> horas = new Hashtable<String, Integer>();
	static Hashtable<String, Integer> horas2 = new Hashtable<String, Integer>();
	public static void pais1(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\horasBra.txt");
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
				//System.out.println(lines.charAt(0));
				nDeTweets1 = nDeTweets1 +1; 
				String[] partes = lines.split(",");
				System.out.println(partes[0]);
				if (horas2.get(partes[0])== null){
					horas2.put(partes[0], 1);
					
				}
				else{
				valor = horas2.get(partes[0]) ;
				valor = valor +1;
				horas2.put(partes[0], valor);
				}
				


			}
			tweetsPais1 = Pais1 + ":" + String.valueOf(nDeTweets1);
			//System.out.println("Francia"+"1:" +hora1F +" "+"2:" +hora2F +" "+"3:"+ hora3F);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void pais2(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\horaMex.txt");
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
			
			while( ( lines = file2.readLine()) != null) {
				//System.out.println(lines.charAt(0));
				nDeTweets2 = nDeTweets2 +1; 
				String[] partes = lines.split(",");
				System.out.println(partes[0]);
				if (horas.get(partes[0])== null){
					horas.put(partes[0], 1);
				}
				else{
				valor = horas.get(partes[0]) ;
				valor = valor +1;
				horas.put(partes[0], valor);
				}
				
				

			}
			System.out.println(horas);
			tweetsPais2 = Pais2 + ":" + String.valueOf(nDeTweets2);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}
}



