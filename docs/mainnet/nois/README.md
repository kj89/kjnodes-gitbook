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

**live-peers** (29)
```bash
peers="b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,171b9d4700909ec297641aa8a69d45b4149f0d1d@141.94.193.28:55726,271dd7f12a4d9d5b1b740dcb90c55b756bf69dbf@74.50.74.98:26656,017ba5ab50dc434356740630d5d64d20063e8d32@54.39.128.229:26636,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,dac094230205ee1f49b42ac0ace9d95c3578d7e7@88.198.18.88:32656,3ca7cbc2cd1938d67b50ae27447f9a975e39f58e@94.130.16.254:36656,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,22ec344512fc679e16eb358284e0d1eaa4291194@142.132.253.112:36656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,3784e5ecd7f703c8a37427463e9c7c7b31389345@142.132.211.91:51656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,d4f30672ef58f234fd13b503f7ca3d32ffc4e7a2@45.63.104.164:26656,8e0b3f56137f0fb116e13575c7805c1a975d8306@93.186.200.10:51656,533bff9f712beefd9e17066f1c71414fc70335e6@213.202.208.101:26656,c5d5d9dbcf99488ea0f45054806b3604fc98bd4e@113.161.144.108:26656,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,00852ba0bfdf20aac74369b1a5c43e50668c9738@135.181.128.114:17356,33f354ba808b12dbc389511172d283863fdfed11@162.55.245.219:51656,4194a82db2d4ed54641d8b4a926fc71411e7aad9@202.61.194.254:60756,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
