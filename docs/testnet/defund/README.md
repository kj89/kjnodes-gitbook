# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (25)
```bash
peers="7c36aa2b2b84492121000b0b35398853b2443a42@38.242.140.2:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,feaf23d0c4e2726e823cbd275acbef74df8333cf@165.22.218.21:26656,9e67baeac323278617e9036a892464b21dfe3a38@65.108.71.92:45656,9389cefdaa999eb81b93f4354d1077553ceb7a86@217.76.55.76:26656,d27958fc8f9841733f9ecf0beec8d36e51519828@65.108.153.138:26656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,7b85da5bbdd0c88e7165ef4272e3edc68254f90e@154.12.231.14:26656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,8190bf19ef96627e3b35f2039ab6aeed551fa05c@167.235.201.57:26656,16af5142a97d6bd22f941c15ad8faf2150d48e59@157.90.157.18:26656,9cbaf117258ac247bce37f314d1a2ddba34b5ad6@194.163.190.54:26656,2a87e54d6849058523a0d761318cb1258c4299df@77.91.123.14:26656,d368e8fc76143f89e53f0997fd5dfef32129168c@109.110.63.204:26656,5db1142851dd1c7106779aa9d348a9f67a630df0@164.68.110.234:26656,ad9e3e6b195c3238463c030ed08db814465a1d9e@77.232.37.54:26656,1a2166e8c08130d678cae0bc88cfabc8b6ed8d78@178.18.244.17:26656,f9fd8aff0825e7c5fb76f7b6f42a4a2bbbdb04f7@84.46.244.224:26656,fb73921dc5bf1e939308eaa37053c12bd647852b@45.147.199.210:26656,6c0024b454c7e001b98ab04692c9d616d403bb7d@176.9.146.72:40656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,0d190196414307625a087a2d3cd02756fb4643a7@65.108.13.185:26767"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
