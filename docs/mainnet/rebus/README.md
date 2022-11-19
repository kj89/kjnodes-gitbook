# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (29)
```
peers="1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,e6e888332d1930e24daecbe587500de6360f41cb@65.108.104.253:26656,408206e3aab058d1dc09697566e3dadfaa3760ea@135.181.5.47:20106,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,17779ded6b3dc2f31d6c6f40cc6f07d802753ba7@78.47.153.128:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,8f023504e27873141164b6fbf1c4b788ff8d533b@159.69.200.24:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,f968f06c0f9c08cf7c9ccaf933cc903023ebcc24@194.163.167.122:26656,f4ad005ee8ec25508c498294e9e83d81b188ea49@185.248.24.16:21656,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,f0d73a4976e64643ffc6d3fc335725902b795491@162.248.225.244:26656,98206a8f71578850f1d88f08ede96ebc7e7c76a9@176.9.188.21:52656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,0a3eb0b5a76b2b881ae260e4546e3fbbfbbfba4b@65.108.206.56:32656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,7ee74ea68e350fc5214657255cba5e339bb30c2a@138.201.127.91:26674,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,e04e8466071f8f00defce1d45c27ca6118bac358@135.125.4.73:54556,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@144.76.163.233:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
