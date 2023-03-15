# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="62f7aaafd73816bdaf685a6270541c1d1f8162ad@155.133.27.170:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,f1d30c5f2d5882823317718eb4455f87ae846d0a@85.239.235.235:30656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,b594f01b5b49a11b6d2e97c3b6358dc1388a1039@65.108.108.52:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
