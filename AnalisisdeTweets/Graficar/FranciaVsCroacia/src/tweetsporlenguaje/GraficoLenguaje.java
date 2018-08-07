package tweetsporlenguaje;

import java.awt.BorderLayout;
import java.awt.Color;
import java.io.File;
import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JPanel;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;


public class GraficoLenguaje extends JFrame{
	
		
		


	public static void main(String args[]){
		ObtencionDatosLenguaje OD = new ObtencionDatosLenguaje();
		OD.pais1();
		OD.pais2();
		System.out.println(ObtencionDatosLenguaje.fechasPais2.get("16  ")+"dato de la clave");
		new GraficoLenguaje().setVisible(true);
		// Fuente de Datos
				DefaultCategoryDataset dataset = new DefaultCategoryDataset();
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("th  "), ObtencionDatosLenguaje.tweetsPais1, "Tailandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("it  "), ObtencionDatosLenguaje.tweetsPais1, "Italiano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("pt  "), ObtencionDatosLenguaje.tweetsPais1, "Portugués");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("sl  "), ObtencionDatosLenguaje.tweetsPais1, "Esloveno");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("en  "), ObtencionDatosLenguaje.tweetsPais1, "Inglés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("tl  "), ObtencionDatosLenguaje.tweetsPais1, "Tagalo");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("nl  "), ObtencionDatosLenguaje.tweetsPais1, "Holandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("hu  "), ObtencionDatosLenguaje.tweetsPais1, "Húngaro");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("et  "), ObtencionDatosLenguaje.tweetsPais1, "Estonio");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("fr  "), ObtencionDatosLenguaje.tweetsPais1, "Francés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("is  "), ObtencionDatosLenguaje.tweetsPais1, "Islandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("fi  "), ObtencionDatosLenguaje.tweetsPais1, "Finlandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("tr  "), ObtencionDatosLenguaje.tweetsPais1, "Turco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("lv  "), ObtencionDatosLenguaje.tweetsPais1, "Letón");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("cs  "), ObtencionDatosLenguaje.tweetsPais1, "Checo");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ro  "), ObtencionDatosLenguaje.tweetsPais1, "Rumano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("sv  "), ObtencionDatosLenguaje.tweetsPais1, "Sueco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ca  "), ObtencionDatosLenguaje.tweetsPais1, "Catalán");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ja  "), ObtencionDatosLenguaje.tweetsPais1, "Japonés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("da  "), ObtencionDatosLenguaje.tweetsPais1, "Danés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("hi  "), ObtencionDatosLenguaje.tweetsPais1, "Hindú");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("es  "), ObtencionDatosLenguaje.tweetsPais1, "Español");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("cy  "), ObtencionDatosLenguaje.tweetsPais1, "Galés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ru  "), ObtencionDatosLenguaje.tweetsPais1, "Ruso");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("eu  "), ObtencionDatosLenguaje.tweetsPais1, "Euskera");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("de  "), ObtencionDatosLenguaje.tweetsPais1, "Alemán");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("no  "), ObtencionDatosLenguaje.tweetsPais1, "Noruego");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("und  "), ObtencionDatosLenguaje.tweetsPais1, "Indeterminado");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("lt  "), ObtencionDatosLenguaje.tweetsPais1, "Lituano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("pl  "), ObtencionDatosLenguaje.tweetsPais1, "Polaco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ht  "), ObtencionDatosLenguaje.tweetsPais1, "Haitiano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais.get("ar  "), ObtencionDatosLenguaje.tweetsPais1, "Árabe");
				
				
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ar  "), ObtencionDatosLenguaje.tweetsPais2, "Árabe");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ht  "), ObtencionDatosLenguaje.tweetsPais2, "Haitiano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("th  "), ObtencionDatosLenguaje.tweetsPais2, "Tailandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("it  "), ObtencionDatosLenguaje.tweetsPais2, "Italiano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("pt  "), ObtencionDatosLenguaje.tweetsPais2, "Portugués");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("sl  "), ObtencionDatosLenguaje.tweetsPais2, "Esloveno");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("en  "), ObtencionDatosLenguaje.tweetsPais2, "Inglés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("tl  "), ObtencionDatosLenguaje.tweetsPais2, "Tagalo");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("nl  "), ObtencionDatosLenguaje.tweetsPais2, "Holandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("hu  "), ObtencionDatosLenguaje.tweetsPais2, "Húngaro");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("et  "), ObtencionDatosLenguaje.tweetsPais2, "Estonio");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("fr  "), ObtencionDatosLenguaje.tweetsPais2, "Francés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("is  "), ObtencionDatosLenguaje.tweetsPais2, "Islandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("fi  "), ObtencionDatosLenguaje.tweetsPais2, "Finlandés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("tr  "), ObtencionDatosLenguaje.tweetsPais2, "Turco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("pl  "), ObtencionDatosLenguaje.tweetsPais2, "Polaco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("lv  "), ObtencionDatosLenguaje.tweetsPais2, "Letón");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("cs  "), ObtencionDatosLenguaje.tweetsPais2, "Checo");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("lt  "), ObtencionDatosLenguaje.tweetsPais2, "Lituano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ro  "), ObtencionDatosLenguaje.tweetsPais2, "Rumano");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("sv  "), ObtencionDatosLenguaje.tweetsPais2, "Sueco");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ca  "), ObtencionDatosLenguaje.tweetsPais2, "Catalán");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ja  "), ObtencionDatosLenguaje.tweetsPais2, "Japonés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("da  "), ObtencionDatosLenguaje.tweetsPais2, "Danés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("hi  "), ObtencionDatosLenguaje.tweetsPais2, "Hindú");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("es  "), ObtencionDatosLenguaje.tweetsPais2, "Español");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("cy  "), ObtencionDatosLenguaje.tweetsPais2, "Galés");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("ru  "), ObtencionDatosLenguaje.tweetsPais2, "Ruso");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("eu  "), ObtencionDatosLenguaje.tweetsPais2, "Euskera");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("de  "), ObtencionDatosLenguaje.tweetsPais2, "Alemán");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("no  "), ObtencionDatosLenguaje.tweetsPais2, "Noruego");
				dataset.setValue(ObtencionDatosLenguaje.fechasPais2.get("und  "), ObtencionDatosLenguaje.tweetsPais2, "Indeterminado");
			
				// Creando el Grafico
				JFreeChart chart = ChartFactory.createBarChart3D
						("Tweets","Lenguaje", "Numero", 
								dataset, PlotOrientation.HORIZONTAL, true,true, false);
				chart.setBackgroundPaint(Color.white);
				chart.getTitle().setPaint(Color.black);
				
				CategoryPlot p = chart.getCategoryPlot(); 
				
				p.setRangeGridlinePaint(Color.gray); 
				// Mostrar Grafico
				   ChartFrame frame = new ChartFrame("JFreeChart", chart);
			        frame.pack();
			        frame.setVisible(true);
				try {

					ChartUtilities.saveChartAsJPEG(new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\FRAVSCROLenguaje.jpg"), chart, 1500, 1500);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
}
