# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: gravitybridge.grpc.kjnodes.com:26090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (14)
```bash
peers="94a09a149acbaf7435d8d4082fd6100598e1fee0@157.90.5.119:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,dc840076d50cf601da3ca708bc3665c7d480ff98@65.108.13.74:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,4e1ea298ef66eec3ec320171f90336a1e4bb13ea@51.81.107.95:10256,930f874c17eff988acd8eb761fea8d4873ea6eb3@185.249.227.231:29656,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,2b107c598194efa2efb04cbd395528900ffb1b1c@65.108.104.113:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,7ec5a1fe29feebb8ff632ebe2a4e3f70586e2adc@65.108.232.134:33656,811817c6ddc112ed37f7cd71c6bbae186f1e8239@135.125.188.17:34095,162e8994c0738fb5895e77b888718ea51d4c40d3@167.86.106.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
