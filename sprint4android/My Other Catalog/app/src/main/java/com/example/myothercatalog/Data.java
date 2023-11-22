package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

//determina la informacion q contiene la celda
public class Data {
    private String name;
    private String imageUrl;

    public Data(JSONObject json) { //aqui me llega cada elemento del json y yo "filtro" q datos quiero
        //creo una variable para cada dato que quiero mostrar
        try{
            this.name = json.getString("name");
            this.imageUrl = json.getString("image_url");
        }catch (JSONException e) {
            e.printStackTrace();
        }
    }

    //hago un get para cada uno de los datos q quiero q se muestren
    public String getName() {
        return name;
    }
    public String getImageUrl() {
        return imageUrl;
    }
}
