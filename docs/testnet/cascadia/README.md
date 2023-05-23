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
peers="f47667544d7d5b65f316ba5ab8fca2e81e8fe4f4@157.90.208.222:36656,5d563f5d882904f89b929fde2d1cf2342c8cba7c@185.209.223.64:36656,833214d32a7cec6b7f33816e05cfccf28c2d96f4@31.220.77.241:26656,367d2c06fb155438b7dd6c451973e68ec0c5ac30@185.218.126.179:18656,1168af52cf36c68e2405b3041c8d53ed1ca169be@65.109.158.190:26656,47058eb9ee90cfb0b994a4a82767d3844934ee39@65.108.41.155:26656,577e5876fab3d5f94a43522a58f2fe0f07445599@95.217.211.32:30656,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
