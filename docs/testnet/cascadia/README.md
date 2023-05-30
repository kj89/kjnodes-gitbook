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
peers="780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,fc698cb2ca4daff21f0e4c377503343cc72dd5eb@64.225.100.42:26656,3931d2ddb913c90a0df7b645c529a4804c5faef6@65.108.149.96:18656,4affb0923e1be1f18818db3ababe682c63f6a1e3@65.109.144.236:30656,fc80d9960383e9b441d5217550bf7cbcd2aacbca@38.242.154.155:18656,f78611ffa950efd9ddb4ed8f7bd8327c289ba377@65.109.108.150:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,a4fa41f9104a77cbf5310e3890a64499b8e866e4@91.230.110.190:26656,96fa0a28f5ca7f0263e91ce81be554f7ebb1d85a@167.114.172.204:55656,f4242842d8ab0ba390d16b583ae97d962484e223@38.242.220.255:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
