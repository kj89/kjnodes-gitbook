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
peers="0b4857a716ff7e9a1813c1f069f177e8d0a7c744@85.10.199.157:51656,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,8826663aa6d8f28d53978a8c9b7c940bc0818ae8@65.109.93.100:30656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,3156dc7460480c256fa41fbe377f64fb1bd75aed@45.94.58.246:25656,3ca7cbc2cd1938d67b50ae27447f9a975e39f58e@94.130.16.254:36656,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,22ec344512fc679e16eb358284e0d1eaa4291194@142.132.253.112:36656,1d3861fb38164385d5b98c4cf4e35452bab403cc@149.102.146.216:26656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,00852ba0bfdf20aac74369b1a5c43e50668c9738@135.181.128.114:17356,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,533bff9f712beefd9e17066f1c71414fc70335e6@213.202.208.101:26656,3784e5ecd7f703c8a37427463e9c7c7b31389345@142.132.211.91:51656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,8e0b3f56137f0fb116e13575c7805c1a975d8306@93.186.200.10:51656,f9c01cefd0f119b29b72c96bd84f37bb9d273874@65.108.6.45:61456,40692288807db7ac022e24e9247cd60e7fc995c7@81.0.248.57:17356,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,732fe2553e152d37b29653ee07324fdbfd5ef961@95.217.200.26:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,d4f30672ef58f234fd13b503f7ca3d32ffc4e7a2@45.63.104.164:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
