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
peers="54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,04f999a256386af81147442b05ffd4022313de2c@146.190.116.68:20156,5795a44b9e632d5f24c61fa09a434e487355d0a4@144.91.70.120:30656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,18296589a77b09df6c75559c84815f71fb7add9e@194.163.147.189:26656,433cc64756cb7f00b5fb4b26de97dc0db72b27ca@65.108.216.219:6656,56f709e56ef9e95fcfd9376e28f4afdd1178ca09@65.109.30.90:38656,85953732c4eb5165724ac6db331240ff0815daf1@1.15.104.210:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
