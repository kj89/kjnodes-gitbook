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
peers="7502abfa0929a2469f10696f6f309c7e7c5555ab@95.217.83.28:17356,d2041f5d812b4fb196d5210a287448b68fe7bef9@95.217.104.49:51656,acf21becb9397db3dc7ad29cd11993c8869d0ad3@65.21.52.246:26656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,0cf59ab91e4a96d6e5427d903644edd18d9421d1@142.132.248.138:26786,922d90c7ef1840c984fcfa387a491c8d3c4481dc@65.108.141.109:55656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,5cb88ba0649f0ae6e7bb7df9aa6a630702bd3643@91.107.192.45:26656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,8f36fd1d1b8718e54053b64717ddbbbe2a4e6d3d@154.53.44.239:26656,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,f03752476d5f328b26960e20b6101a68c3c9cd6d@65.109.112.170:27656,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,271dd7f12a4d9d5b1b740dcb90c55b756bf69dbf@74.50.74.98:26656,3aa61724c5fde2d9778346f5f806c41508112ac5@195.154.94.166:26889,732fe2553e152d37b29653ee07324fdbfd5ef961@95.217.200.26:36656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,e84cbe410271d84b2968c46881522bd3e9726898@144.76.30.36:15663,2f03f27d96d7f28de26ab38eac26fe4dbfdccfa8@88.99.164.158:40136"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
