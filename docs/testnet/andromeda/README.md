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
peers="d0ef5f5583ff0343ea41962f68010bff54caafde@212.90.121.45:30656,f17030edb4e4ec7143c3e3bbbfaeee3dd1a619f2@194.34.232.224:56656,0da5e83ef55df6f1c6f8c15c69bdd42ee43fd253@144.76.99.100:30656,e61f287d51edab6f6dbe00a8b804614443ee6f82@80.85.242.117:26656,54188a9dea5ded1d891aa6c3c0e2a403322b1707@178.54.78.180:16656,c4bb11ae43f4db7b8eef312a3c38861d236eb660@91.201.113.194:26656,3d25f45062b5f3f49a87d38300ca0f657a9c853f@84.252.159.238:02656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14756,32e94653d765d9a43eb9c7a97d752dd96b2a50d6@213.247.154.10:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
