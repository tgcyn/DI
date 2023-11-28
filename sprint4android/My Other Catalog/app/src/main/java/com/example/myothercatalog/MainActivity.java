package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;
import java.util.jar.JarException;

public class MainActivity extends AppCompatActivity {
    private Context context;
    private RequestQueue requestQueue;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this;
        requestQueue = Volley.newRequestQueue(this);

        Toast.makeText(this, "Cargando lista", Toast.LENGTH_LONG).show();
        showRecyclerView(); //creo un metodo aparte para q este mejor organizado
    }

    //en este metodo pongo el request
    private void showRecyclerView() {
        RecyclerView recyclerView = findViewById(R.id.recycler_view);
        Activity activity = this;

        context = this;

        //como se trata de una lista, tengo q usar JsonArrayRequest
        JsonArrayRequest request = new JsonArrayRequest(
                Request.Method.GET,
                "https://raw.githubusercontent.com/tgcyn/DI/main/recursos/catalog.json", //dn se guarda la informacion q quiero visualizar
                null,
                new Response.Listener<JSONArray>() { //indica q hacer cnd la peticion es correcta
                    @Override
                    public void onResponse(JSONArray response) {
                        List<Data> allTheBooks = new ArrayList<>(); //creo una list del tipo data para guardar los datos q quiero mostrar
                        for (int i=0; i< response.length(); i++) { //para cada elemento de la liata
                            try{
                                JSONObject libro = response.getJSONObject(i); //creo un objeto con la informacion de ese elemento del json
                                Data data = new Data(libro); //envio el objeto con la informacion para obtener la informacion
                                allTheBooks.add(data); //guardo la informacion obtenida en la lista q voy a mostrar
                            }catch (JSONException e) {
                                e.printStackTrace();
                            }
                        }
                        Adapter adapter = new Adapter(allTheBooks, activity);
                        recyclerView.setAdapter(adapter);
                        recyclerView.setLayoutManager(new LinearLayoutManager(activity));
                    }
                },
                new Response.ErrorListener() { //indica q hacer cnd la peticion falla
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(activity, error.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                }
        );
        this.requestQueue.add(request);
    }
}