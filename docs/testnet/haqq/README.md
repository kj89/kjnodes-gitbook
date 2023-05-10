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

**live-peers** (9)
```bash
peers="442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,b87ae2a43e27bd0360ea1b868c8cb9e98d612fce@65.109.92.79:19656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556,8238ddf162ce8a144610e671c63226b0207a1f73@38.242.148.96:36656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
