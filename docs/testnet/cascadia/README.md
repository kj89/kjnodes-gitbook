# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="10be839bd10e61383523a0b6302b3b056c51dab9@142.132.152.46:13656,42ec68fe0eeeff1bb0ef64e1ae74c99c8d58c293@78.46.106.75:15656,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,04c15c3a102a6fea54e17dc9c11280f8c7f94afd@45.91.168.78:18656,5e00a5323aa21b54669be868f2d2ab1e9d581207@135.181.183.62:18656,956e1b99ceef18f53b12ec7a0db97c350a7457a7@5.161.81.115:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,e9f315c8115ecba182acf4b5d85190e8c1fcef2f@37.27.20.236:18656,950f69c2e21b39357c1aad3ddbb654ac2de4bb3d@161.97.134.203:18656,9ecdb4f8159f1fd727623a69eaf82a04f97e1612@193.187.129.77:18656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
