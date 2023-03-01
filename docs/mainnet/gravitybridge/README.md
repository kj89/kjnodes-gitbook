# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (16)
```bash
peers="ef05d5aca4398f4b217b9bbf08729a1338c67eeb@142.132.193.186:36656,ddf8f9ff250f760228c667d256d16ed4f1880c27@65.109.43.75:27010,0a8487549154b7dd96fd0af1843ecfa62246f816@18.144.134.123:26656,572d417e11368f588d110efdeb7102a6a3c0752d@161.35.224.108:26656,6eb2a2e7bcd82aad56b6652a328c72f148f84935@194.147.58.224:26656,4d82b4d1851982b6eb81e67cb3b5bd040eda7cdc@136.244.29.116:26666,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,2b107c598194efa2efb04cbd395528900ffb1b1c@65.108.104.113:26656,e38de921f46e22de0be8e4eba0b0338cbd065fc9@51.81.159.162:26656,ca4270ebed73b4d0982450aac16fe08860410fac@142.132.248.138:26626,12500973a0561656f86ea12ce3bbf05a48714ad8@35.79.31.168:26656,114180a593e480b0443ca61bb1325289a7029bc6@78.47.198.121:26656,2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656,ca9d9d0605f178fbba3bdf92e13719ab9dce0fc7@23.88.59.82:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
