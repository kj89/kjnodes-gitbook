# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Version Tag**: v1.8.1 | **Wasm**: OFF

[Website](https://www.gravitybridge.net) | [Discord](https://discord.gg/ARV8dTSjAk) | [Twitter](https://twitter.com/gravity_bridge)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/gravitybridge](https://explorer.kjnodes.com/gravitybridge)

## Public endpoints

* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)
* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* grpc: [https://gravitybridge.grpc.kjnodes.com](https://gravitybridge.grpc.kjnodes.com)

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

**live-peers** (12)
```bash
peers="16f40620f1b1942246015f35c40dd9fc84e51b01@66.94.124.27:26656,4d82b4d1851982b6eb81e67cb3b5bd040eda7cdc@136.244.29.116:26666,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,e5362a93c6e7f686d72c8d6d98be2c7bceeb5cc3@49.12.23.149:27010,5ad3fe86b1214e1f5c897d23a2863fb46bdfc1f7@185.16.38.165:14256,56a8349703e8f5c97c452c7e45f5bcaac966ccbf@207.180.204.110:26656,ddf8f9ff250f760228c667d256d16ed4f1880c27@65.109.43.75:27010,c57dcf8e3af80236059194c86a6f81c1735903d6@162.19.89.8:10256,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,a9e9c67632880147aad2517c9ee19cac6d9d052e@193.17.92.212:26656,07e2da0edb0facd81dab948a128330cc1250b24c@193.70.47.90:14256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
