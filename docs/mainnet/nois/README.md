# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-1 | **Latest Version Tag**: v1.0.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisRNG)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/nois/noisvaloper1fe7ju873fkknmfrmytaft93y5rlf0xcrqtp39k) (every 5 minutes)
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
peers="1c69bfe397bf62159ccd5074aaa4c7461d5a034a@88.99.161.162:25656,6ef1914f30ac7becdf2c718b65c61cd618b7021a@57.128.144.242:26656,c094593ce99e795fd913f2f1f9bbb5f90d9b4e3f@91.107.219.161:26656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,922d90c7ef1840c984fcfa387a491c8d3c4481dc@65.108.141.109:55656,fcb9c69549185c252e70a1910ab7f4bf81f43b32@65.21.203.204:51656,6eb54f48d03c2da8ab354c99ba25c80ccdeb5127@37.27.0.53:26656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,5cb88ba0649f0ae6e7bb7df9aa6a630702bd3643@91.107.192.45:26656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,171b9d4700909ec297641aa8a69d45b4149f0d1d@141.94.193.28:55726,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,3aa61724c5fde2d9778346f5f806c41508112ac5@195.154.94.166:26889,3daa2128d58d812f63a0c0cf5d19aeb14f811928@65.109.28.226:03656,acf21becb9397db3dc7ad29cd11993c8869d0ad3@65.21.52.246:26656,763f4cd38f0685616b6657d9a34c1cdbf01ca90c@212.23.222.109:26456,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,8cce0e919b1a7c42086a712748c8e84d7d7cd9ac@135.181.155.14:26656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,0ec27f38fed1fb128df1353782e92b4c13b90db9@167.160.93.90:56656,23d7872bdd8b1bf80b52cb20da57b88a4935bc3d@65.109.30.197:22656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
