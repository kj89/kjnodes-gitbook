# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/andromeda.png" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: andromeda-testnet.grpc.kjnodes.com:14790

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:14756
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:14759
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (9)
```bash
peers="c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,5e5186020063f7f8a3f3c6c23feca32830a18f33@65.109.174.30:56656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,4d4309bf054ca12f128035eab81b66350b5de575@178.172.212.122:26656,e66db5c342d1800fa734f679407089096c0fdb0c@146.19.233.253:26656,3c68a8074d2bfa2e5a4af81c64833871b3fa10f6@38.242.225.219:26656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
