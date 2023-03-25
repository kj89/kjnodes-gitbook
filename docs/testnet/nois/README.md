# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nois.png" width="150" alt=""><figcaption></figcaption></figure>

Nois Network aims to bring randomness (or noise)  to the Cosmos ecosystem by providing a safe and  secure entropy source and distributing randomness  in the form of random beacons to other Cosmos blockchains via IBC.

**Chain ID**: nois-testnet-004 | **Latest Version Tag**: v0.6.0 | **Wasm**: ON

[Website](https://nois.network) | [Discord](https://discord.gg/dHdpwtEb6F) | [Twitter](https://twitter.com/NoisNetwork)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nois-testnet](https://explorer.kjnodes.com/nois-testnet)

## Public endpoints

* api: [https://nois-testnet.api.kjnodes.com](https://nois-testnet.api.kjnodes.com)
* rpc: [https://nois-testnet.rpc.kjnodes.com](https://nois-testnet.rpc.kjnodes.com)
* grpc: nois-testnet.grpc.kjnodes.com:51090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nois-testnet.rpc.kjnodes.com:51656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nois-testnet.rpc.kjnodes.com:51659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nois-testnet/addrbook.json > $HOME/.noisd/config/addrbook.json
```

**live-peers** (18)
```bash
peers="1a1086d1c1c671b1e3e3e189c495318594f3a0a3@144.76.30.36:15648,72cd4222818d25da5206092c3efc2c0dd0ec34fe@161.97.96.91:36656,f2315b5ce33cb2d2e0e4098dbf593b23710e995f@38.242.221.64:30656,91f2416b553b819b904c7e2b7823af3a7885e4d2@65.108.158.51:26656,bfbd43dbfbcda81b6d63f47e211f9d8eb323811c@65.109.39.50:26656,c86b0c3ffb4fa65b188ac68d2872a9d91559bce1@65.21.55.133:26656,b1692b30c971fd105d5a44194a414ddc6e1d2f13@65.109.227.120:26656,12c80b97e746b47b7b753aad9f3d85edab279957@104.193.254.42:27656,85c6416dbac30808521ccfc31a59047238cd8fe3@65.109.112.20:11104,f4ed6f6bdf086cbaab9bed20e4dfc1daf326e4fc@89.117.50.54:26656,7b94b17a9eb14e1e263c20e4f395a4b0f0bc1978@192.95.30.128:26656,0845590c7b9ac5d3a9813d1e06dfdf76c49f5876@142.132.209.236:17356,55b593887e758eeb7c1c6e3f8ffd8b30eabd0069@65.108.82.62:26656,c53187e34d66494bb5ec89445008fad4a8517c83@65.109.5.235:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:51656,40250630b11b62814410129ed5dc29221e141a2f@65.108.72.233:26156,a87dc8b4e827a05fe5c46aea54999120c8252587@162.19.237.81:26656,7bf392b33faa03a68c83c933623c84cdfbcb5a0e@178.63.8.245:60656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.noisd/config/config.toml
```
