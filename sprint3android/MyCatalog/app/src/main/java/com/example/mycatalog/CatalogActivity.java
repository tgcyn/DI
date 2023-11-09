package com.example.mycatalog;

import androidx.annotation.NonNull;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import com.google.android.material.navigation.NavigationView;

public class CatalogActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener{
    private Context context;
    private DrawerLayout drawerLayout;
    private ActionBarDrawerToggle actionBarDrawerToggle;
    private Toolbar toolbar;
    private NavigationView navigationView;
    private FragmentTransaction fragmentTransaction;
    private FragmentManager fragmentManager;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        context = this;

        /* EJERCICIO 2
        Button b1 = findViewById(R.id.primerButton); //creo una instancia button para ligarlo con el escrito en el xml

        b1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) { //este metodo indica q, cuando se pulse el boto, haga la accion especificada
                Intent intent = new Intent(context, DetailActivity.class); //intent permite abrir la segunda actividad, tengo q dar dos parámetros: 1)la clase en la q estoy (context) 2)la clase q quiero iniciar (DetailActivity) espsdificada como clase (.class)
                startActivity(intent); //esto hace q empiece la actividad
            }
        });
        */

        //EJERCICIO 5
            //1. crear un archivo layout drawer_header q va a ser el nombre del menu una vez desplegado
            //2. crear un archivo layout drawer_toolbar
            //3. crear un archivo layout containt_main q va a ser el contenedor de los fragment
            //4. crear un nuevo android resource file drawer_menu en res, type menu (el menu va a ser realmente un listado de los fragments)
            //5. crear un item para cada elemento del menu
            //6. en el layout ligado a la actividad, añadimos dos include (toolbar y container) para mostrarlos en la actividad y un NavigationView
            //7. al navigationView tengo q añadirle el menu y el header para q se muestren al desplegarlo (el NavigationView es lo q va a hacer q veamos los fragment como el menu q estamos acostumbrados a ver)
            //8. cambiar DetailActivity y AboutActivity a extends Fragments y hacer el metodo onCreateView para poder trabajar con ellos en el drawer_menu
        // una vez hemos hecho eso, ya podemos empezar a trabajar en la actividad

            //instanciamos el toolbar con el ID
        toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        drawerLayout = findViewById(R.id.drawer);

        navigationView = findViewById(R.id.navigationView);
            //establecer el equivalente al onClick de cada fragment
        navigationView.setNavigationItemSelectedListener(this);

        actionBarDrawerToggle = new ActionBarDrawerToggle(this, drawerLayout, toolbar, R.string.open, R.string.close);
        drawerLayout.addDrawerListener(actionBarDrawerToggle);
        actionBarDrawerToggle.setDrawerIndicatorEnabled(true);
        actionBarDrawerToggle.syncState();

            //cargar primer fragment (PrimeraPantalla)
        fragmentManager = getSupportFragmentManager();
        fragmentTransaction = fragmentManager.beginTransaction();
        fragmentTransaction.add(R.id.container, new PrimeraPantalla());
        fragmentTransaction.commit();

    }

    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            //para q una vez se haya clickeaddo en algun fragment el toolbar se cierre automaticamente
        drawerLayout.closeDrawer(GravityCompat.START);

            //vamos a usar el ID de cada fragment/item para saber a q actividad corresponde
        if (item.getItemId() == R.id.aboutActivity){
                //reemplazar el fragment actual por el correspondiente a AboutActivity
            fragmentManager = getSupportFragmentManager();
            fragmentTransaction = fragmentManager.beginTransaction();
            fragmentTransaction.replace(R.id.container, new AboutActivity());
            fragmentTransaction.commit();
        }

        if (item.getItemId() == R.id.detailActivity){
                //reemplazar el fragment actual por el correspondiente a DetailActivity
            fragmentManager = getSupportFragmentManager();
            fragmentTransaction = fragmentManager.beginTransaction();
            fragmentTransaction.replace(R.id.container, new DetailActivity());
            fragmentTransaction.commit();
        }

        return false;
    }
}