import { describe, it, expect } from 'vitest';
import { pmoskills, inject } from '../src';

describe('PMOSkills SDK Test Suite', () => {
  describe('Executable Skills', () => {
    it('should load all 48 executable skills', () => {
      const skills = pmoskills.getSkills();
      expect(skills.length).toBe(48);
    });

    it('should retrieve a specific skill by ID and have correct metadata', () => {
      const skill = pmoskills.getSkill('SKL-01-01');
      expect(skill).toBeDefined();
      expect(skill?.id).toBe('SKL-01-01');
      expect(skill?.title).toBe('Establish PM Governance Framework');
      expect(skill?.metadata.domain).toBe('Governance');
      expect(skill?.template).toContain('## Purpose');
    });

    it('should support filtering skills by performance domain', () => {
      const governanceSkills = pmoskills.getSkillsByDomain('Governance');
      expect(governanceSkills.length).toBeGreaterThan(0);
      expect(governanceSkills[0].metadata.domain).toBe('Governance');
    });
  });

  describe('Process Records', () => {
    it('should load all 41 PMBOK 8 process records', () => {
      const processes = pmoskills.getProcesses();
      expect(processes.length).toBe(41);
    });

    it('should retrieve a specific process by ID and contain parsed lists', () => {
      const process = pmoskills.getProcess('PR01');
      expect(process).toBeDefined();
      expect(process?.id).toBe('PR01');
      expect(process?.title).toBe('Develop Project Charter');
      expect(process?.inputs).toContain('Business Documents');
      expect(process?.outputs).toContain('Project Charter');
      expect(process?.tools).toContain('Expert Judgment');
    });
  });

  describe('System Prompts and Ontology', () => {
    it('should load pre-defined system prompts correctly', () => {
      const orchestrator = pmoskills.getSystemPrompt('pmo-orchestrator');
      expect(orchestrator).toBeDefined();
      expect(orchestrator?.title).toContain('Master PMO Orchestrator');
      expect(orchestrator?.prompt).toContain('You are the PMOSkills Master PMO Orchestrator');
    });

    it('should retrieve the ontology specification', () => {
      const ontology = pmoskills.getOntology();
      expect(ontology).toBeDefined();
      expect(ontology.id).toBe('pmoskills-ontology');
      expect(ontology.content).toContain('# 🧠 PMOSkills Knowledge Graph & Ontology Specification');
    });
  });

  describe('Prompt Template Injector', () => {
    it('should inject variables into {{ brace }} format placeholders', () => {
      const template = 'Hello {{ name }}! Welcome to {{ projectName }}.';
      const result = inject(template, { name: 'Alice', projectName: 'Helios' });
      expect(result).toBe('Hello Alice! Welcome to Helios.');
    });

    it('should inject variables into [FIELD: variable] format placeholders', () => {
      const template = 'Execute [FIELD: skillName] for project [FIELD:projectId].';
      const result = inject(template, { skillName: 'Charter Setup', projectId: 'PRJ-101' });
      expect(result).toBe('Execute Charter Setup for project PRJ-101.');
    });

    it('should inject variables into [variable] format placeholders', () => {
      const template = 'Authorize [role] to manage [scope].';
      const result = inject(template, { role: 'PMO Director', scope: 'Governance Baseline' });
      expect(result).toBe('Authorize PMO Director to manage Governance Baseline.');
    });
  });
});
