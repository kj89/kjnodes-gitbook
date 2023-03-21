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

**live-peers** (15)
```bash
peers="114180a593e480b0443ca61bb1325289a7029bc6@78.47.198.121:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,c4385ec685f08dfd635df6d21be9dfbdfdb52896@161.97.182.71:26656,a460c9af789a48396a2f5ee62e3f7e79a6b84d4f@46.38.243.16:26656,f750840e55b48690e6078fca417dace5433a2e8b@65.108.135.212:23656,ddf8f9ff250f760228c667d256d16ed4f1880c27@65.109.43.75:27010,7a05c69e10c76348e4fadeda5e0803ff4804e183@188.34.180.92:26656,74efecf52ba78626d4ba796fb6073fa9cb26b19e@65.108.11.250:26656,a9e9c67632880147aad2517c9ee19cac6d9d052e@193.17.92.212:26656,2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656,70ff1535443969705182c9473cc66773fbc12c09@15.235.13.145:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,3eae7c785e7038b3c1376dc2fc8e6cff9d0ad709@65.108.121.110:14656,c4666a5c897463492246983fdc78ab20f32dc0c0@50.21.167.179:26656,df243a4c65b436fb4c81bf71b83ce9de865fea5a@213.239.207.165:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gravity/config/config.toml
```
