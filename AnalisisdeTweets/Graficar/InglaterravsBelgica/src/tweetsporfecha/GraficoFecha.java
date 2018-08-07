package tweetsporfecha;

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


public class GraficoFecha extends JFrame{


	public static void main(String args[]){
		ObtencionDatosFecha OD = new ObtencionDatosFecha();
		OD.pais1();
		OD.pais2();
		//System.out.println(ObtencionDatosFecha.fechasPais2.get("16  ")+"dato de la clave");
		new GraficoFecha().setVisible(true);
		
		DefaultCategoryDataset dataset = new DefaultCategoryDataset();
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jun 28  "), ObtencionDatosFecha.tweetsPais1, "Jun28");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jun 28  "), ObtencionDatosFecha.tweetsPais2, "Jun28");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jun 29  "), ObtencionDatosFecha.tweetsPais1, "Jun29");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jun 29  "), ObtencionDatosFecha.tweetsPais2, "Jun29");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jun 30  "), ObtencionDatosFecha.tweetsPais1, "Jun30");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jun 30  "), ObtencionDatosFecha.tweetsPais2, "Jun30");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jun 31  "), ObtencionDatosFecha.tweetsPais1, "Jun31");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jun 31  "), ObtencionDatosFecha.tweetsPais2, "Jun31");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 01  "), ObtencionDatosFecha.tweetsPais1, "Jul01");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 01  "), ObtencionDatosFecha.tweetsPais2, "Jul01");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 02  "), ObtencionDatosFecha.tweetsPais1, "Jul02");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 02  "), ObtencionDatosFecha.tweetsPais2, "Jul02");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 03  "), ObtencionDatosFecha.tweetsPais1, "Jul03");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 03  "), ObtencionDatosFecha.tweetsPais2, "Jul03");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 04  "), ObtencionDatosFecha.tweetsPais1, "Jul04");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 04  "), ObtencionDatosFecha.tweetsPais2, "Jul04");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 05  "), ObtencionDatosFecha.tweetsPais1, "Jul05");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 05  "), ObtencionDatosFecha.tweetsPais2, "Jul05");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 06  "), ObtencionDatosFecha.tweetsPais1, "Jul06");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 06  "), ObtencionDatosFecha.tweetsPais2, "Jul06");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 07  "), ObtencionDatosFecha.tweetsPais1, "Jul07");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 07  "), ObtencionDatosFecha.tweetsPais2, "Jul07");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 08  "), ObtencionDatosFecha.tweetsPais1, "Jul08");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 08  "), ObtencionDatosFecha.tweetsPais2, "Jul08");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 09  "), ObtencionDatosFecha.tweetsPais1, "Jul09");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 09  "), ObtencionDatosFecha.tweetsPais2, "Jul09");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 10  "), ObtencionDatosFecha.tweetsPais1, "Jul10");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 10  "), ObtencionDatosFecha.tweetsPais2, "Jul10");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 11  "), ObtencionDatosFecha.tweetsPais1, "Jul11");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 11  "), ObtencionDatosFecha.tweetsPais2, "Jul11");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 12  "), ObtencionDatosFecha.tweetsPais1, "Jul12");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 12  "), ObtencionDatosFecha.tweetsPais2, "Jul12");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 13  "), ObtencionDatosFecha.tweetsPais1, "Jul13");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 13  "), ObtencionDatosFecha.tweetsPais2, "Jul13");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 14  "), ObtencionDatosFecha.tweetsPais1, "Jul14");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 14  "), ObtencionDatosFecha.tweetsPais2, "Jul14");
		dataset.setValue(ObtencionDatosFecha.fechasPais.get("Jul 15  "), ObtencionDatosFecha.tweetsPais1, "Jul15");
		dataset.setValue(ObtencionDatosFecha.fechasPais2.get("Jul 15  "), ObtencionDatosFecha.tweetsPais2, "Jul15");
		
	
		// Creando el Grafico
		JFreeChart chart = ChartFactory.createBarChart3D
				("Tweets","Fecha", "Numero", 
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

			ChartUtilities.saveChartAsJPEG(new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\INGVSBELfechas.jpg"), chart, 1500, 1500);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
