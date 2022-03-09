import javax.management.RuntimeErrorException;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.util.Scanner;
import java.security.NoSuchAlgorithmException;

public class GUI {
    public static String filename;

    public GUI() {

        JFrame frame = new JFrame("MD5");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);

        JPanel panel = new JPanel();
        frame.add(panel);

        // Select File
        JButton selectfile = new JButton("Select File");
        JButton Process = new JButton("Process");
        panel.add(selectfile);
        panel.add(Process);

        selectfile.addActionListener(new ActionListener() {
            // final String filename;
            @Override
            public void actionPerformed(ActionEvent ae) {
                // final String filename;
                JFileChooser button = new JFileChooser();
                button.setCurrentDirectory(new File(System.getProperty("user.home")));
                int result = button.showSaveDialog(null);

                if (result == JFileChooser.APPROVE_OPTION) {
                    File selectedFile = button.getSelectedFile();
                    filename = selectedFile.getAbsolutePath();
                }
            }
        });

        Process.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent ae) {

                int lines = 0;
                File file = new File(filename);

                try {
                    BufferedReader reader = new BufferedReader(new FileReader(filename));
                    while (reader.readLine() != null)
                        lines++;
                    reader.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                Object data_values[][] = new Object[lines][2];
                try {
                    Scanner file_read = new Scanner(file);
                    int i=0;
                    while(file_read.hasNextLine()){
                        String data = file_read.nextLine();
                        String[] value = data.split("-");
                        String s = "";
                        for (int j = 0; j < value.length - 1; j++) {
                            if (j == 0)
                                s += value[j];
                            else
                                s += ("-" + value[j]);
                        }
                        String hashValue = MD(s.replaceAll("\\s", ""));
                        String hashText = value[value.length -1].replaceAll("\\s", "");

                        data_values[i][0] = s.replaceAll("\\s", "");
                        if(hashValue.equals(hashText))
                            data_values[i][1] = "verified";
                        else
                            data_values[i][1] = "not verified";
                        
                        i++;
                    }
                    file_read.close(); 
                    
                    //Show Table
                    JFrame frame2 = new JFrame();
                    JPanel panel2 = new JPanel();
                    panel2.setLayout(new BorderLayout());

                    DefaultTableModel model = new DefaultTableModel();
                    model.addColumn("Plain-Text");
                    model.addColumn("Result");

                    JTable table = new JTable(model);
                    JScrollPane tableContainer = new JScrollPane(table);
                    
                    panel2.add(tableContainer, BorderLayout.CENTER);
                    frame2.getContentPane().add(panel2);

                    for (int j = 0; j < data_values.length; j++) {
                        model.addRow(new Object[]{data_values[j][0], data_values[j][1]});
                    }

                    frame2.pack();
                    frame2.setVisible(true);
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (NoSuchAlgorithmException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    protected String MD(String input) throws NoSuchAlgorithmException {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(input.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);
            String hashtext = no.toString(16);

            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
            return hashtext;
        } catch (Error e) {
            throw new RuntimeErrorException(e);
        }
    }

    public static void main(String[] args) {
        new GUI();  
    }
}
