package com.mitocode.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import com.mitocode.model.*;
import com.mitocode.model.ProductoChiper;

public interface ITiendaRepo extends JpaRepository<Tienda, String>{

}
