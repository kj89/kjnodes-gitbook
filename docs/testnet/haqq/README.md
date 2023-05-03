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
peers="b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,18603aa0e749211298227974b7d3b7724cb9bb8d@185.16.38.136:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13556,0d600b8281ee6a710c213023755d2382cf90af13@116.202.165.116:46656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,a6150d39e4725d28a56f41ebf3c6d457c54bd2f1@34.138.250.4:26656,afe8c5af90e2eef4a98bc998366e2e780a927599@65.108.126.46:34656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
