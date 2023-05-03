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
peers="717066f5726fb3cd7096f84911c7c8bfe5953e62@81.68.158.68:26656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,e95899eb682e517d74449dd575073daf1a3266d5@135.181.208.169:27656,362ede6f335ed641e9eba0057bc1d98b391751dd@65.108.54.29:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,99cebda3a65a35b9a6a8bef774c8b92c1e548aa5@65.108.226.26:36656,3b998a882d8d9bcb2869eef988af86254e0e9602@89.116.29.20:26656,4a369367f8ee97c976330f9be79da387d11a0340@65.108.194.44:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,27752331150b966e3082e8dd8b364693379c1129@212.41.9.98:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
