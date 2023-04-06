# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)



Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois](https://explorer.kjnodes.com/nois)

## Public endpoints

* api: [https://nois.api.kjnodes.com](https://nois.api.kjnodes.com)
* rpc: [https://nois.rpc.kjnodes.com](https://nois.rpc.kjnodes.com)
* grpc: nois.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:51656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="23d7872bdd8b1bf80b52cb20da57b88a4935bc3d@65.109.30.197:22656,a1b7affbe008c5e900c5b2e1598aa212215fa3cb@144.76.176.154:51656,f03752476d5f328b26960e20b6101a68c3c9cd6d@65.109.112.170:27656,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,68eff0c3e5cf5fa259851e50d3af5f1f2f8bd42c@135.181.215.62:4830,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,3ca7cbc2cd1938d67b50ae27447f9a975e39f58e@94.130.16.254:36656,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,563162895c3152ba7c46b115cd79f5d75017e9dc@65.108.138.80:17356,5538f2c7fdbf5e1c71f456c07f863d82ee814935@95.217.154.80:26656,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,00852ba0bfdf20aac74369b1a5c43e50668c9738@135.181.128.114:17356,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,732fe2553e152d37b29653ee07324fdbfd5ef961@95.217.200.26:36656,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,7e62349bfecba01be593cb5c62f0b3fd1af3e813@65.109.81.119:50656,ad53e98a88aa0c6f724b457ad6575b83c5f4a02b@167.235.15.19:30656,64bb3218e9e71177e3a72bcc5f36c9f9cc654f7b@51.68.204.169:26656,7275b1b0a0bf7867906a3f182604456af2360897@185.144.99.65:16656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,017ba5ab50dc434356740630d5d64d20063e8d32@54.39.128.229:26636"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
