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

**live-peers** (10)
```bash
peers="b2bdcd106645c538f86f24f7a3f253d8e1bf34ab@217.76.57.54:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656,8083dd301a7189284bf5b8d40c4cf239360d653a@5.9.122.49:26656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,03603fb96ded3aabe7451efad31fb8d0c523a0ee@146.19.75.97:26656,717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
