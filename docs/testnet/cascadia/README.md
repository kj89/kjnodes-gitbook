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
peers="2aa27e0a6952b333b06df43d071126de2f4ce490@185.182.185.171:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,fc80d9960383e9b441d5217550bf7cbcd2aacbca@38.242.154.155:18656,f55eaf24fe87dfe4c5feb64ba2e2f5b730901927@185.255.131.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,0a460700e6e087887bca7c4657e3fb1b676297fa@217.76.56.58:18656,9955217431ad3b081e06938d792426a8c4a1a0d5@95.216.172.187:18656,bce4f77a3339c033c95ae96cab73f642c4d15fd5@185.187.169.105:55656,f2a5f1a90fd0b9f9cf85223ddc78a4b936f26d5d@95.217.72.99:39656,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
