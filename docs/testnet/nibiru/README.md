# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Wasm**: OFF

Website: [https://nibiru.fi](https://nibiru.fi)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (9)
```
peers="b32bb87364a52df3efcbe9eacc178c96b35c823a@135.181.115.111:27656,80d976ce69962409fc5e0b8a756f26eaad001102@178.238.229.107:36656,6b7c6b9519331f8c4a57e5f27c2c4fe291a09f19@14.29.132.178:26656,41af2131870b3a6ef50bc3d420ed8a58b5cd3073@194.5.152.47:26656,ae357e14309640ca33cde597b37f0a91e63a32bd@144.76.90.130:36656,d45505ae0cae35d12599364cf035e7dda3a7be09@194.5.152.43:26656,456c75e3d465d34a22a976afb17e96e85947de75@167.99.36.201:26656,cccc4ded4edc583eac49165b5265619e23e55d0f@38.242.156.249:26656,dae1c8e4b46bba38d7903797fa63d266ae8188f8@150.158.90.74:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
