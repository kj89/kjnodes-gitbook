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

**live-peers** (18)
```bash
peers="c66e5cc02d87731faf781463466bf39723d4558b@68.183.181.120:26656,ea0c590882f4fa490a4563e364d341e078ad138e@94.131.105.228:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,3f9594221efe3e9cd4d0de31f71993fc0f12bf01@65.21.245.252:26656,bb81a52f86a5332e447373796f8a0b99f195816d@5.78.67.243:26656,4d4ef8f6ff2f1ac8ba5e102e858f6ecbd0d3dda1@31.220.84.3:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,704e605f9bd65912d8c65a58f955601c31188548@65.21.203.204:19656,443a51f595c9ca16273ca6146db1375e4223a91f@172.93.110.154:26656,e5a2bcbcea7d3b2ea7d7feb75da1c115125b665f@65.109.112.178:31656,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,2e6164a7c45c1840494af5db9bc54aacc39a065e@85.239.233.241:26656,7ff2aaa5c49a0907e52689cc90fa416ec70e06a4@185.245.182.152:30656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
