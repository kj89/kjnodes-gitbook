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
peers="f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,3ba8280c245f4d63a8f7913aea64a5071f0c76d7@65.109.18.166:54656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,331ca63236ba05842d561e22c0bcc8582efa60a1@209.126.80.192:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
