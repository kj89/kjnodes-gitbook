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

**live-peers** (11)
```bash
peers="d3c2ce714e2c803d8686a0101711bf7164f844be@62.171.146.21:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,f58c0d432b28ebefb7573ab23cb394e67098c347@209.126.81.240:26636,b9836aff6d8e79b9a04b4a2a80d6007bf33a526b@198.244.179.125:32069,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,20248068f368f5d1eda74646d2bfd1fcdaffb3e1@89.58.59.75:60656,56f709e56ef9e95fcfd9376e28f4afdd1178ca09@65.109.30.90:38656,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,3969b8ddc6d0ed9f2deb0265e4b26e88c5cb894a@149.102.150.250:30656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,c06d5254e4ecb69ccae41feff4d75de2dd92154d@149.102.138.176:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
