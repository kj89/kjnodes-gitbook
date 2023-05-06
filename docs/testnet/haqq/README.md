# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:13590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:13556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:13559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (10)
```bash
peers="3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,8238ddf162ce8a144610e671c63226b0207a1f73@38.242.148.96:36656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
