package com.cmcg.investor.users.controllers;

import com.cmcg.investor.users.models.Investor;
import com.cmcg.investor.users.services.InvestorService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import java.util.Arrays;
import java.util.List;

import static org.mockito.Mockito.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(InvestorController.class)
public class InvestorControllerTest {

    @MockBean
    private InvestorService investorService;

    private MockMvc mockMvc;

    @InjectMocks
    private InvestorController investorController;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        mockMvc = MockMvcBuilders.standaloneSetup(investorController).build();
    }

    @Test
    void createInvestorSuccessfully() throws Exception {
        Investor investor = new Investor();
        Investor createdInvestor = new Investor();
        when(investorService.saveInvestor(investor)).thenReturn(createdInvestor);

        mockMvc.perform(post("/api/investors")
                        .contentType("application/json")
                        .content("{\"name\":\"John Doe\",\"type\":\"Individual\",\"entityNo\":\"12345\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("John Doe"));

        verify(investorService, times(1)).saveInvestor(any(Investor.class));
    }

    @Test
    void getInvestorByIdSuccessfully() throws Exception {
        Long investorId = 1L;
        Investor investor = new Investor();
        when(investorService.getInvestorById(investorId)).thenReturn(investor);

        mockMvc.perform(get("/api/investors/{id}", investorId))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.id").value(investorId));

        verify(investorService, times(1)).getInvestorById(investorId);
    }

    @Test
    void updateInvestorSuccessfully() throws Exception {
        Long investorId = 1L;
        Investor investor = new Investor();
        Investor updatedInvestor = new Investor();
        when(investorService.saveInvestor(investor)).thenReturn(updatedInvestor);

        mockMvc.perform(put("/api/investors/{id}", investorId)
                        .contentType("application/json")
                        .content("{\"name\":\"Jane Doe\",\"type\":\"Corporate\",\"entityNo\":\"67890\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("Jane Doe"));

        verify(investorService, times(1)).saveInvestor(any(Investor.class));
    }

    @Test
    void deleteInvestorSuccessfully() throws Exception {
        Long investorId = 1L;
        doNothing().when(investorService).deleteInvestor(investorId);

        mockMvc.perform(delete("/api/investors/{id}", investorId))
                .andExpect(status().isNoContent());

        verify(investorService, times(1)).deleteInvestor(investorId);
    }

    @Test
    void getAllInvestorsSuccessfully() throws Exception {
        List<Investor> investors = Arrays.asList(new Investor(), new Investor());
        when(investorService.getAllInvestors()).thenReturn(investors);

        mockMvc.perform(get("/api/investors"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.length()").value(investors.size()));

        verify(investorService, times(1)).getAllInvestors();
    }
}