# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" alt=""><figcaption></figcaption></figure>

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
* grpc: nois.grpc.kjnodes.com:15190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@nois.rpc.kjnodes.com:15156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@nois.rpc.kjnodes.com:15159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="017ba5ab50dc434356740630d5d64d20063e8d32@54.39.128.229:26636,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15156,533bff9f712beefd9e17066f1c71414fc70335e6@213.202.208.101:26656,ae02b0a36568a1f2be71bd98840aae333d1e3147@51.159.195.168:46656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27286,23d7872bdd8b1bf80b52cb20da57b88a4935bc3d@65.109.30.197:22656,379c0e32463be66e5cf8d13d62eb87ddb1a702c2@142.132.152.46:47656,83e530ade685efa61579eccd9f990462cd0ff36e@5.189.157.124:21656,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
