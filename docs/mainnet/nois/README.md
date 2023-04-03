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
peers="0ede37f273933f5f9d6644f68e51128c6332c431@65.108.11.234:26656,b8711d88e017e33753a59abd9e202744ddf3f9a5@148.251.8.186:33656,ae02b0a36568a1f2be71bd98840aae333d1e3147@51.159.195.168:46656,47e99c3e8bbd881952cf4a642c8c2c8d178f56de@51.79.77.103:36656,95eeb1ac374e4144b05b36f6c5986472e7ef698f@135.181.209.51:26786,3ca7cbc2cd1938d67b50ae27447f9a975e39f58e@94.130.16.254:36656,b5058b5422c6bdba55eafac46cc23731288f42c8@130.255.170.126:26656,9d21af60ad2568ffcb55a0bd0eb03b6cfa2644c5@49.12.120.113:26656,a5224f7375f156c07c28f336355e4e727699fad5@65.109.95.26:27656,8ec2fee6c37c07cc5af57ec870015a0191d4707d@65.108.65.36:51656,1c69bfe397bf62159ccd5074aaa4c7461d5a034a@88.99.161.162:25656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,c98c58a8cd821f8814bb995d30299e76abb485aa@142.132.194.157:26456,9620f8453f34270be5fa3d458968d8bd1c997430@95.70.184.178:29656,b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,3156dc7460480c256fa41fbe377f64fb1bd75aed@45.94.58.246:25656,23d7872bdd8b1bf80b52cb20da57b88a4935bc3d@65.109.30.197:22656,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,f03752476d5f328b26960e20b6101a68c3c9cd6d@65.109.112.170:27656,374615fcb23cfbd30a59a2b904cf675d9b93b7e0@78.46.61.117:01656,ad53e98a88aa0c6f724b457ad6575b83c5f4a02b@167.235.15.19:30656,8669164aadd01c6024ecb286932350f77603da9b@104.193.254.42:27656,5538f2c7fdbf5e1c71f456c07f863d82ee814935@95.217.154.80:26656,f9c01cefd0f119b29b72c96bd84f37bb9d273874@65.108.6.45:61456,eb3bbea0e9247b157e4d5ac40373d0370d49905c@113.161.144.108:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:51656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
