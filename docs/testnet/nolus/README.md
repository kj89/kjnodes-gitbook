# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: OFF

Website: [https://www.nolus.io](https://www.nolus.io)


## Public endpoints

* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (9)
```
peers="1a0bb6c35e2663202535d4b849ff06250762d299@213.239.216.252:35656,1a5f37caaa5dd174bc2797bf2a70b804e71bc632@162.55.42.27:26656,c6e7b095d965209c8d15086c2a173627fb9b29e1@161.97.169.22:26656,3c4f8aa4bf226c331b32d93f51f089e47e753279@194.163.155.84:36656,89aaf76a23b16bd57a1982e7b304fd998a49942a@65.109.85.226:9000,7ebb5ef5cb8a00e3bc2f3b89be89fdf8854d9cdf@51.79.102.215:26656,17cc34fc4a5c91e67bc7e11b9c15cad10dd11336@138.201.221.94:26656,33d485f51f413fd4bf83ef8a971c10228a39cffb@62.171.161.172:26656,d694df8e90ddf6102be5c825e57fc58d55217629@143.198.205.193:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nolus/config/config.toml
```
