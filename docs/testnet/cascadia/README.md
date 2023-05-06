# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

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
peers="37f1c41be15a41e33a0a820d55db3ca439486602@148.251.90.138:18656,244cb3a0c72cfd0a6abd138fb9a3982ff85aeaf3@217.76.49.183:26656,b7500cabcb081a22abf4d712a7d19536861f25e3@194.163.148.202:55656,f2b1bcee05c1986a2cd88293337491c1bc249a9d@188.191.36.222:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,42ec68fe0eeeff1bb0ef64e1ae74c99c8d58c293@78.46.106.75:15656,3124aff7052b93976636b16d1c50e82a214fd6ee@65.109.155.215:26656,af8b5486e4938c3bd9ab56fd5ee03d26857089a1@31.220.95.213:26656,a47973f2e731fc35ea0f1e2d115b51ee77b91827@109.123.249.188:26656,b7588e5718e25a1486257dda9bfe08e3032e1043@91.107.213.196:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
