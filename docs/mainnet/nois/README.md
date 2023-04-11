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
peers="2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,483678c263d8ceb45b11e450628928d05c641187@194.163.167.138:60656,1893178693fc4e376f8c093ae30e44e27619f79c@198.244.213.94:25156,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,5cb88ba0649f0ae6e7bb7df9aa6a630702bd3643@91.107.192.45:26656,bc09ae5db2c015cdf7caad44d1d724dd1cf59f29@74.208.94.42:26646,1c69bfe397bf62159ccd5074aaa4c7461d5a034a@88.99.161.162:25656,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,271dd7f12a4d9d5b1b740dcb90c55b756bf69dbf@74.50.74.98:26656,0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,922d90c7ef1840c984fcfa387a491c8d3c4481dc@65.108.141.109:55656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,ad53e98a88aa0c6f724b457ad6575b83c5f4a02b@167.235.15.19:30656,23d7872bdd8b1bf80b52cb20da57b88a4935bc3d@65.109.30.197:22656,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,763f4cd38f0685616b6657d9a34c1cdbf01ca90c@212.23.222.109:26456,5538f2c7fdbf5e1c71f456c07f863d82ee814935@95.217.154.80:26656,0cf59ab91e4a96d6e5427d903644edd18d9421d1@142.132.248.138:26786,1ff95efbb1fc681ab3302e8da70370c6e4f1462f@65.108.130.171:26656,acf21becb9397db3dc7ad29cd11993c8869d0ad3@65.21.52.246:26656,b99339ba925e39489aea4b1d2a86f15eced1f88e@89.233.108.86:36656,171b9d4700909ec297641aa8a69d45b4149f0d1d@141.94.193.28:55726,40692288807db7ac022e24e9247cd60e7fc995c7@81.0.248.57:17356,c5d5d9dbcf99488ea0f45054806b3604fc98bd4e@113.161.144.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
