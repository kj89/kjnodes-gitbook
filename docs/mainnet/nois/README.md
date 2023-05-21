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

**live-peers** (11)
```bash
peers="b26e5ac4afbadf96ad31ee3aeb5e6557f2894037@65.108.199.222:30656,eb9f7a7afefd583e8fd7c63858812a83eeb19974@65.21.205.248:51656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,533bff9f712beefd9e17066f1c71414fc70335e6@213.202.208.101:26656,8f36fd1d1b8718e54053b64717ddbbbe2a4e6d3d@154.53.44.239:26656,c695f41458b08fe87729beffa513f1c38d20d1db@193.70.33.64:17356,dd7607ce23081b71310137221ebe4610c3114bea@57.128.20.163:17356,0cf59ab91e4a96d6e5427d903644edd18d9421d1@142.132.248.138:26786,2e1d9305a5be27fc708ea7bc2fade939be1259e6@65.108.82.62:51656,288e7a14ccac3cdc1d8ab20335d4c48edf5930f2@84.46.250.136:17356,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:15156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
