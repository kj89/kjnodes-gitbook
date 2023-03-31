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
peers="0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,72cd4222818d25da5206092c3efc2c0dd0ec34fe@161.97.96.91:36656,47e99c3e8bbd881952cf4a642c8c2c8d178f56de@51.79.77.103:36656,3ca7cbc2cd1938d67b50ae27447f9a975e39f58e@94.130.16.254:36656,fefa1d14781af7cd0067c3fe14f8c119cc9afadf@38.146.3.180:17356,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,a1b7affbe008c5e900c5b2e1598aa212215fa3cb@144.76.176.154:51656,732fe2553e152d37b29653ee07324fdbfd5ef961@95.217.200.26:36656,22ec344512fc679e16eb358284e0d1eaa4291194@142.132.253.112:36656,d4f30672ef58f234fd13b503f7ca3d32ffc4e7a2@45.63.104.164:26656,7502abfa0929a2469f10696f6f309c7e7c5555ab@95.217.83.28:17356,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,d2041f5d812b4fb196d5210a287448b68fe7bef9@95.217.104.49:51656,239b2ca49200a05ea9bda83c1e201ae4bcd9dd6f@31.220.87.206:51656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,acf21becb9397db3dc7ad29cd11993c8869d0ad3@65.21.52.246:26656,171b9d4700909ec297641aa8a69d45b4149f0d1d@141.94.193.28:55726,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,6d514b525db3a3a010848648a35c7118b844b330@65.108.44.149:46656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,3c5926d0b4b8750f16f6495063e6d762b2556d1e@65.21.122.47:27656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,eb3bbea0e9247b157e4d5ac40373d0370d49905c@113.161.144.108:26656,8cc5b14d9146a5318577003506c6624433d813f1@5.78.99.23:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,fcb9c69549185c252e70a1910ab7f4bf81f43b32@65.21.203.204:51656,ad53e98a88aa0c6f724b457ad6575b83c5f4a02b@167.235.15.19:30656,c8db99691545545402a1c45fa897f3cb1a05aea6@65.108.231.124:36656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
