# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Binary Version**: v1.7.2 | **Wasm**: OFF

Website: [https://www.gravitybridge.net](https://www.gravitybridge.net)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```
peers="381c0aabfa183467858bd4e1f2071b1b0a77e94c@142.132.154.39:26656,e5a11a1a8a36f0910755d0fc3546e8e3198283da@18.156.199.4:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,b2608e51a520866a91637ca3b354903bc5b46bfa@137.184.214.71:26656,a23523a46e1c6beefde15210f419407c59c5f6f2@31.7.207.16:26656,f750840e55b48690e6078fca417dace5433a2e8b@65.108.135.212:23656,32ec6bad2b67212d2cde5e01554cd2d22940ce03@142.132.154.176:26656,46374f308b7cbf6a8d8242bad8666760b433cb9d@62.171.164.145:26656,002aa595555a41de38f3816f10e5cced923757b3@34.223.93.26:26656,39490daffac0c7847b0d2617e412b2942055a82b@95.214.53.46:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
